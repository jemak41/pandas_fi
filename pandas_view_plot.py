from pandas_view import *


def baselining(base,lim):
    baseline = []
    z = 1
    while z <= lim:
        baseline.append(base)
        z += 1
    return baseline

class plotting:
    mark = '--'
    mark2 = '-'
    if x == 1:
        plt.figure(1)

        plt.subplot(2,2,1)
        plt.plot(repm.Month, baselining(32000, len(repm)),'r--')
        plt.plot(repm.Month, repm.Price,'b-')
        #plt.plot(repm.Month.loc[0:len(repm) - 2], baselining(40000,len(repm) - 1),'r--', linewidth=4.0)
        #plt.plot(repm.Month.loc[0:len(repm) - 2], repm.Price.loc[0:len(repm) - 2],'b-', linewidth=4.0)
        plt.title('RECURRING Expenses per month')


        plt.subplot(2,2,2)
        plt.plot(nrepm.Month, baselining(40000, len(nrepm)),'r--')
        plt.plot(nrepm.Month, nrepm.Price,'b-')
        plt.title('NON-RECURRING Expenses per month')

        plt.subplot(2,2,(3,4))
        plt.plot(tepm.Month, baselining(72000, len(tepm)),'r--')
        plt.plot(tepm.Month, tepm.Price,'b-')
        plt.title('TOTAL Expenses per month')

        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.style.use('classic')
        plt.show()

        plt.figure(2)

        plt.subplot(3,2,(1,3))
        plt.plot(nrepm.Month, baselining(50000, len(nrepm)),'r--')
        plt.plot(nrepm.Month, nrepm.Price,'b-')
        plt.title('NON-RECURRING Expenses per month')

        plt.subplot(3,2,2)
        plt.plot(nepm.Month, nepm.Price,'b-')
        plt.title('NECESSARRY Expenses per month')

        plt.subplot(3,2,5)
        plt.plot(lepm.Month, lepm.Price,'b-')
        #plt.plot(lepm.Month, baselining(40000, len(lepm)),'r--')
        plt.title('LUHO Expenses per month')

        plt.subplot(3,2,(4,6))
        plt.plot(bepm.Month, bepm.Price,'b-')
        plt.title('BUSINESS Expenses per month')

        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()



        plt.figure(3)
        ax = plt.subplot(111)
        ax.set_facecolor('xkcd:grey')
        #colors = bgrcmyk

        plt.plot(metepm1.Month, metepm1.Price,'b' + mark, label=metepm1.TypeName.max(),linewidth=4,markersize=15)
        plt.plot(metepm2.Month, metepm2.Price,'g' + mark, label=metepm2.TypeName.max(),linewidth=4,markersize=15)
        #plt.plot(metepm3.Month, metepm3.Price,'r' + mark, label=metepm3.TypeName.max())
        plt.plot(metepm4.Month, metepm4.Price,'r' + mark, label=metepm4.TypeName.max(),linewidth=4,markersize=15)
        plt.plot(metepm6.Month, metepm6.Price,'c' + mark, label=metepm6.TypeName.max(),linewidth=4,markersize=15)
        plt.plot(metepm7.Month, metepm7.Price,'g' + mark2, label=metepm7.TypeName.max(),linewidth=4,markersize=15)
        plt.plot(metepm8.Month, metepm8.Price,'y' + mark, label=metepm8.TypeName.max(),linewidth=4,markersize=15)
        #plt.plot(metepm9.Month, metepm9.Price,'b' + mark, label=metepm9.TypeName.max())
        plt.plot(metepm10.Month, metepm10.Price,'k' + mark, label=metepm10.TypeName.max(), linewidth=4,markersize=15)
        #plt.plot(metepm11.Month, metepm11.Price,'r' + mark2, label=metepm11.TypeName.max())
        plt.plot(metepm13.Month, metepm13.Price,'b' + mark2, label=metepm13.TypeName.max(), linewidth=4,markersize=15)
        plt.plot(metepm14.Month, metepm14.Price,'m' + mark, label=metepm14.TypeName.max(), linewidth=4,markersize=15)
        plt.plot(metepm15.Month, metepm15.Price,'w' + mark, label=metepm15.TypeName.max(), linewidth=4,markersize=15)
        #plt.plot(metepm16.Month, metepm16.Price,'k' + mark2, label=metepm16.TypeName.max(), markersize=15)

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('Monthly Expenses by Type Name')
        plt.margins(.02)
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()

    elif x == 2:

        plt.figure(1)
        plt.subplot(1, 1, 1)
        plt.plot(tipm.Month, baselining(100000, len(tipm)), 'r--')
        plt.plot(tipm.Month, tipm.Price, 'b-')
        # plt.plot(repm.Month.loc[0:len(repm) - 2], baselining(40000,len(repm) - 1),'r--', linewidth=4.0)
        # plt.plot(repm.Month.loc[0:len(repm) - 2], repm.Price.loc[0:len(repm) - 2],'b-', linewidth=4.0)
        plt.title('Total Income per month')
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()

        plt.figure(2)
        ax = plt.subplot(111)
        ax.set_facecolor('xkcd:grey')
        plt.plot(metipm1.Month, metipm1.Price, 'r' + mark, label=metipm1.TypeName.max(), linewidth=4, markersize=15)
        plt.plot(metipm2.Month, metipm2.Price, 'c' + mark, label=metipm2.TypeName.max(), linewidth=4, markersize=15)
        plt.plot(metipm3.Month, metipm3.Price, 'g' + mark, label=metipm3.TypeName.max(), linewidth=4, markersize=15)
        plt.plot(metipm4.Month, metipm4.Price, 'y' + mark, label=metipm4.TypeName.max(), linewidth=4, markersize=15)
        plt.plot(metipm5.Month, metipm5.Price, 'k' + mark, label=metipm5.TypeName.max(), linewidth=4, markersize=15)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('Monthly Income by Type Name')
        plt.margins(.02)
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()
